<?php

namespace App\Http\Controllers;

use App\Models\Scores;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Spatie\PdfToImage\Pdf;
use Intervention\Image\ImageManagerStatic as Image;
use Madnest\Madzipper\Madzipper;
use Illuminate\Support\Facades\File;


class ScoreController extends Controller
{
    public function index()
    {
        $scores = Scores::where('user_id', auth()->id())->get();

        return inertia('Scores/Index', compact('scores'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'file' => 'required|file|mimes:zip',
        ]);
    
        $file = $request->file('file');
        $zipPath = $file->storeAs('public/scores', $file->getClientOriginalName());
    
        // 新規ディレクトリを作成する
        $directory = 'public/scores/' . uniqid();
        Storage::makeDirectory($directory);
    
        // ZIPファイルを展開する
        $madzipper = new Madzipper();
        $madzipper->make(storage_path('app/' . $zipPath))->extractTo(storage_path('app/' . $directory));
    
        // サブディレクトリのパスを作成
        $subDirectoryPath = storage_path('app/' . $directory . '/' . pathinfo($zipPath, PATHINFO_FILENAME));
    
        // 画像ファイルのパスを再帰的に取得する
        $imageFiles = File::allFiles($subDirectoryPath);
    
        // 画像ファイルを保存し、データベースに記録する
        $imagePaths = [];
        foreach ($imageFiles as $imageFile) {
            $filename = $imageFile->getFilename();
            $relativePath = str_replace(storage_path('app/'), '', $imageFile->getPathname());
    
            // 画像ファイルのパスを配列に追加する
            $imagePaths[] = $relativePath;
        }
    
        // Score::create をループの外に移動
        Scores::create([
            'user_id' => auth()->id(),
            'title' => $request->input('title'),
            'file_path' => $directory,
            'image_path' => json_encode($imagePaths),
        ]);
    
        return redirect()->route('scores.index');
    }
    public function edit(Scores $score)
    {
        return Inertia::render('Scores/Edit', compact('score'));
    }

    public function update(Request $request, Scores $score)
    {
        $request->validate([
            'title' => 'required|string|max:255',
        ]);

        $score->update([
            'title' => $request->input('title'),
        ]);

        return redirect()->route('scores.index');
    }

    public function destroy(Scores $score)
    {
        $score->delete();
        Storage::delete($score->file_path);

        return redirect()->route('scores.index');
    }
}