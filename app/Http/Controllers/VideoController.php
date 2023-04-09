<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Video;

class VideoController extends Controller
{
    public function store(Request $request)
    {
        $request->validate([
            'video' => 'required|video|max:2048',
        ]);

        $path = $request->file('video')->store('public/videos');

        return response()->json(['path' => Storage::url($path)]);
    }
    

    public function index()
    {
        $images = Image::all();
        return inertia('Videos', ['videos' => $videos]);
    }
}
