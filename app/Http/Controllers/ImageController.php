<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Image;

class ImageController extends Controller
{
    public function store(Request $request)
    {
        $request->validate([
            'image' => 'required|image|max:2048',
        ]);

        $path = $request->file('image')->store('public/scores');

        return response()->json(['path' => Storage::url($path)]);
    }
    

    public function index()
    {
        $images = Image::all();
        return inertia('Images', ['images' => $images]);
    }
}
