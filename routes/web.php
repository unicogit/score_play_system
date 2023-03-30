<?php

use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Controllers\CallenderController;
use App\Http\Controllers\PlayViewController;
use App\Http\Controllers\PracticesController;
use App\Http\Controllers\PythonController;
use App\Http\Controllers\UploadController;
use App\Http\Controllers\RecordController;

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
    return Inertia::render('Index', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
        'laravelVersion' => Application::VERSION,
        'phpVersion' => PHP_VERSION,
    ]);
});

// Route::get('/dashboard', function () {
//     return Inertia::render('Dashboard');
// })->name('dashboard');
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
        return Inertia::render('Playview');
    })->name('Playview');
    Route::get('/python', [PythonController::class, 'python']);
});
Route::get('/api/positions', [PlayViewController::class, 'fetchPositions'])->name('fetch.positions');


Route::get('/playview', [PlayViewController::class, 'index']);

Route::resource('/record', RecordController::class, ['names' => 'record']);
Route::get('/record', [RecordController::class, 'index']);
Route::post('/record/create', [RecordController::class, 'create']);
Route::post('/record/destroy', [RecordController::class, 'destroy']);

Route::resource('/upload', UploadController::class, ['names' => 'upload']);
Route::get('/upload', [UploadController::class, 'index']);

