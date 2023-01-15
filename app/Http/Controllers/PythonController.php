<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PythonController extends Controller
{
    public function python(Request $request)
    {
        $pythonPath =  "../app/Python/";
        $command = "python" . $pythonPath . "hello.py";
        
        // コマンドを実行
        exec($command, $outputs, $return);
        
        
    }
}
