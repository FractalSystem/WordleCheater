# WordleCheater – Wordle Solution Generator

Unlike the numerous existing Wordle solution finders this application does not seek to solve Wordle puzzles directly, but rather reverse-engineers the Wordle source to determine the solution on any given day.

Wordle selects the daily solution from a corpus of 2315 five letter words locally using a deterministic algorithm to ensure all users of the website have the same puzzle every day.

Contrary to best practices, which would suggest that this should be done server-side to preserve the scarcity of solutions (a key draw of Wordle), this action is performed locally each time a user loads the website.

## This Program

This script will generate daily Wordle solutions for an arbitary time period, due to the deterministic nature of Wordle's puzzle selection algorithm.

Running `generate_solutions.py` on at least Python 3.9 will by generate 10,000 future solutions and 20 previous solutions (including today's) for validation. 

Solutions from 1 January 2022 to May 2049 are saved in the file `generated_solutions.txt` and will remain valid provided Wordle does not adjust its selection algorithm. This can be verified by checking the generated solution for today and comparing it to the live Wordle game [See here](https://www.powerlanguage.co.uk/wordle/)

## How It Works

To generate today's solution the script `wordle_cheater.py` performs the following actions:

1. A list of the 2315 words extracted from Wordle's source is loaded from `data/wordle_words.json`
2. The number of days between 19 June 2021 and today's date is calculated
3. An index `i` is generated with:
```(the number of days from step 2) % (length of the Wordle words list)```
4. The day's solution is the word at the generated index of Wordle's word list

## Javascript magic

The day's solution can also be extracted directly from your browser by entering the following code into the address bar of your browser while on the [Wordle page](https://www.powerlanguage.co.uk/wordle/)

```javascript:alert(new wordle.bundle.GameApp().solution)```

Note that most modern browsers will require that the `javascript:` section of the code is manually typed (rather than pasted)