<?php

namespace App\Http\Controllers;

use App\Events\RecordingStart;
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
        $message = $request->message;
        //送信者を含めてメッセージを送信
        event(new RecordingStart($message));
        return redirect()->back()->with('success', 'recording started');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //remaining columns
        //'time',
        //'score',
        //'output',
        $title = $request->input('title');
        echo($title);
        $video = $request->file('video');
        $created_at = now()->timestamp;
        $path = $video->store('public/videos');
        $url = Storage::url($path);

        Practice::create([
            'title' => $title,
            'video' => $url,
            'created_at' => $created_at,
        ]);
        return redirect()->back()->with('success', 'video uploaded');
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
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
