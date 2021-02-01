tr ["\n"] [" "] < silence_phones.txt > extra_questions.txt
echo  >>  extra_questions.txt
tr ["\n"] [" "] < nonsilence_phones.txt >> extra_questions.txt
echo  >>  extra_questions.txt