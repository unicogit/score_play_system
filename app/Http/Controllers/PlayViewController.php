<?php

namespace App\Http\Controllers;

use App\Models\Practice;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;
use Inertia\Inertia;

class PlayViewController extends Controller
{
    function index(Request $request){
        $practices = Practice::all();
        return Inertia::render(('PlayView'), [
            'practices' => $practices,
        ]);
    }
    public function fetchPositions(Request $request) 
    {
        $contents_array = \File::get(public_path('index.txt'));
        $points_array = \File::get(public_path('point.txt'));
        $contents_split = explode("\n", $contents_array);
        $points_split = explode("\n", $points_array);

        $timestamp = [];
        $points = [];

        foreach ($contents_split as $content) {
            $val = array_map('floatval', explode(',', $content));
            $timestamp[] = $val;
        }

        foreach ($points_split as $point) {
            $val = array_map('intval', explode(',', $point));
            $points[] = $val;
        }

        return [
            'timestamp' => $timestamp,
            'points' => $points,
        ];
    }
}
