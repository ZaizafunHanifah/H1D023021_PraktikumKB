:- dynamic(jawaban/1).

% Dimensi MBTI: E-I, S-N, T-F, J-P

% Pertanyaan per dimensi
pertanyaan(ei, ekstrovert).
pertanyaan(ei, introvert).
pertanyaan(sn, sensing).
pertanyaan(sn, intuition).
pertanyaan(tf, thinking).
pertanyaan(tf, feeling).
pertanyaan(jp, judging).
pertanyaan(jp, perceiving).

% Teks pertanyaan
teks_pertanyaan(ekstrovert, "Apakah Anda merasa nyaman bersosialisasi dengan banyak orang?").
teks_pertanyaan(introvert, "Apakah Anda lebih suka menyendiri untuk mengisi energi kembali?").

teks_pertanyaan(sensing, "Apakah Anda lebih suka informasi yang konkret dan faktual?").
teks_pertanyaan(intuition, "Apakah Anda tertarik pada kemungkinan dan ide-ide masa depan?").

teks_pertanyaan(thinking, "Apakah Anda membuat keputusan berdasarkan logika dan konsistensi?").
teks_pertanyaan(feeling, "Apakah Anda membuat keputusan berdasarkan perasaan dan nilai pribadi?").

teks_pertanyaan(judging, "Apakah Anda suka jadwal dan rencana yang teratur?").
teks_pertanyaan(perceiving, "Apakah Anda lebih suka fleksibilitas dan spontanitas dalam hidup Anda?").

% Aturan untuk menentukan tiap huruf
dimensi(ei, 'E') :- jawaban(ekstrovert), !.
dimensi(ei, 'I') :- jawaban(introvert), !.
dimensi(sn, 'S') :- jawaban(sensing), !.
dimensi(sn, 'N') :- jawaban(intuition), !.
dimensi(tf, 'T') :- jawaban(thinking), !.
dimensi(tf, 'F') :- jawaban(feeling), !.
dimensi(jp, 'J') :- jawaban(judging), !.
dimensi(jp, 'P') :- jawaban(perceiving), !.

% Gabungkan hasil
mbti(Tipe) :-
    dimensi(ei, E),
    dimensi(sn, S),
    dimensi(tf, T),
    dimensi(jp, J),
    atom_concat(E, S, ES),
    atom_concat(ES, T, EST),
    atom_concat(EST, J, Tipe).
