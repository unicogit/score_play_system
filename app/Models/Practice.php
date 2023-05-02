<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Practice extends Model
{
    use HasFactory;
    protected $fillable = [
        'id',
        'user_id',
        'title',
        'practice_date',
        'time',
        'score_id',
        'video',
    ];
    public function scores()
    {
        return $this->belongsTo(Scores::class);
    }
}
