<?php

use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Controllers\CallenderController;
use App\Http\Controllers\PracticeController;
use App\Http\Controllers\PythonController;
use App\Http\Controllers\UploadController;
use App\Http\Controllers\PlayViewController;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return Inertia::render('Welcome', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
        'laravelVersion' => Application::VERSION,
        'phpVersion' => PHP_VERSION,
    ]);
});

Route::get('/dashboard', function () {
    return Inertia::render('Dashboard');
})->name('dashboard');
// Route::redirect('/dashboard', '/callender');

Route::middleware([
    'auth:sanctum',
    config('jetstream.auth_session'),
    'verified',
])->group(function () {
    Route::resource('/callender', CallenderController::class)
        ->names(['index'=>'callender.index',
                'show' => 'callender.show',
                'create' => 'callender.create',
                'edit' => 'callender.edit',
                'update' => 'callender.update',
                'destroy' => 'callender.destroy',
                'store'=>'callender.store',
                'python'=>'callender.python']);
    Route::get('/playview', function () {
        return Inertia::render('PlayView');
    })->name('PLayVideo');
    Route::get('/python', [PythonController::class, 'python']);
});

Route::get('/record', function(){
    return Inertia::render('Record');
});
Route::get('/api/positions', [PlayViewController::class, 'fetchPositions'])->name('fetch.positions');

Route::resource('/upload', UploadController::class)
        ->names(['index'=>'upload.index',
                'show' => 'upload.show',
                'create' => 'upload.create',
                'edit' => 'upload.edit',
                'update' => 'upload.update',
                'destroy' => 'upload.destroy',
                'store'=>'upload.store']);
