<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;
use \App\Models\Callender;
use \App\Models\Practice;

class CallenderController extends Controller
{
    
    public function index(Request $request)
    {       
        $practices = Practice::get();
            return Inertia::render(
                'Callender',
                [
                    'practices'=>$practices
                ]
            );  
    }

    public function create()
    {
        $practice = Practice::get();
        return Inertia::render(
            
            'CallenderCreate',
            [
                'practice'=>$practice,
            ]
        );
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'id' => '',
            'title' => '',
            'practice_date' => '',
            'time' => '',
            'video' => '',
            'score' => '',
        ],[
            'title.required' => 'タイトルを入力してください。',
        ]);
        Practice::create($validated);
        return redirect()->route('callender.index');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $practice = Practice::findOrFail($id);

        return Inertia::render('Callender/Show', [
            'data' => $practice,
        ]);
    }

    // /**
    //  * Show the form for editing the specified resource.
    //  *
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function edit($id)
    // {
    //     $callenders = Callender::get();
    //     $callender = $callenders->where('id', $id)->first();
    //     return Inertia::render(
    //         'CallenderEdit',
    //         [
    //             'id' => $id,
    //             'callender' => $callender,
    //         ]
    //     );
    // }

    // /**
    //  * Update the specified resource in storage.
    //  *
    //  * @param  \Illuminate\Http\Request  $request
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function update(Request $request, $id)
    // {
    //     $callender = Callender::findOrFail($id);
    //     $validated = $request->validate([
    //             'category_id' => '',
    //             'title' => 'required',
    //             'text' => '',
    //             'publish_flag' => '',
    //             'publish_begin' => '',
    //             'publish_end' => '',
    //     ],[
    //         'category_id.required' => 'カテゴリーを選択してください。',
    //         'title.required' => 'タイトルを入力してください。',
    //     ]);
    //     $callender->update($validated);
    //     return redirect()->route('callender.edit',$id);
    // }

    // /**
    //  * Remove the specified resource from storage.
    //  *
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function destroy($id)
    // {
    //     $callender = Callender::findOrFail($id);
    //     try {
    //         $callender->delete();
    //         return redirect()->route('callender.index');
    //     } catch (\Throwable $th) {
    //         return redirect(route('callender.edit', $id))
    //             ->with('errorCode', ErrorCode::NOT_DELETE);
    //     }
    // }
    public function python(Request $request)
    {
        $pythonPath =  "../app/Python/";
        $command = "python" . $pythonPath . "hello.py";
        
        // コマンドを実行
        exec($command, $outputs, $return);
        
        
    }
}
