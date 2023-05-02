<?php

use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Controllers\CallenderController;
use App\Http\Controllers\PlayViewController;
use App\Http\Controllers\PythonController;
use App\Http\Controllers\UploadController;
use App\Http\Controllers\RecordController;
use App\Http\Controllers\ImageController;
use App\Http\Controllers\GatherController;
use App\Http\Controllers\ScoreController;
use App\Http\Controllers\PracticeController;

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
    return Inertia::render('Home', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
        'laravelVersion' => Application::VERSION,
        'phpVersion' => PHP_VERSION,
    ]);
});

Route::get('/dashboard', function () {
    return Inertia::render('Dashboard');
})->name('dashboard');
Route::redirect('/dashboard', '/callender');

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

    Route::resource('/score', ScoreController::class)
        ->names(['index'=>'scores.index',
                'show' => 'scores.show',
                'create' => 'scores.create',
                'edit' => 'scores.edit',
                'update' => 'scores.update',
                'destroy' => 'scores.destroy',
                'store'=>'scores.store']);   
   
    Route::get('/playview', function () {
        return Inertia::render('Playview');
    })->name('Playview');
    Route::get('/python', [PythonController::class, 'python']);
    Route::get('/gather', [GatherController::class, 'index']);

// Route::resource('/record', RecordController::class, ['names' => 'record']);
    Route::get('/record/{userID}/{lessonName}', [RecordController::class, 'index'])->name('record');
    Route::post('/record/create', [RecordController::class, 'create'])->name('record.create');
    Route::post('/record/store', [RecordController::class, 'store'])->name('record.store');
    Route::post('/record/upload', [RecordController::class, 'upload'])->name('record.upload');
    Route::resource('/upload', UploadController::class, ['names' => 'upload']);
    Route::get('/upload', [UploadController::class, 'index']);

    Route::post('/upload-image', [ImageController::class, 'store'])->name('upload-image');
    Route::post('/upload-video', [ImageController::class, 'store'])->name('upload-video');
    Route::get('/images', [ImageController::class, 'index'])->name('images');

    Route::get('/practices/create', [PracticeController::class, 'create'])->name('practices.create');
   
});
Route::get('/api/positions', [PlayViewController::class, 'fetchPositions'])->name('fetch.positions');
Route::get('/recording', function () {
    return Inertia::render('SimpleRecord');
});



