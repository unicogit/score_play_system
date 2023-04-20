<?php

namespace App\Http\Controllers;

use App\Events\RecordingStart;
use App\Events\UploadBlob;
use App\Library\Blob;
use App\Library\RecordMessage;
use App\Models\Practice;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Inertia\Inertia;

class RecordController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return Inertia::render('Record');
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create(Request $request)
    {
        $status = $request->input('status');

        $message = new RecordMessage;
        $message->status = $status;
        //送信者を含めてメッセージを送信
        RecordingStart::dispatch($message);
        return $request;
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // $item = $request->input('video');

        // $blob = new Blob;
        // $blob->video = $item;

        // UploadBlob::dispatch($blob);
        // return $request;
        //remaining columns
        //'time',
        //'score',
        //'output',
        //$title = $request->input('title');
        $video = $request->file('video');
        $title = $request->input('title');
        $practice_date = $request->input('practice_date');
        $created_at = now()->timestamp;
        //videosにstoreしながらパスを取得
        $path = $video->store('public/videos');
        $url = Storage::url($path);

        Practice::create([
            ///'title' => $title,
            'video' => $url,
            'title' => $title,
            'practice_date' => $practice_date,
            'created_at' => $created_at,
        ]);
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function upload()
    {
        UploadBlob::dispatch();
    }
}
