*:
	cat *

dep:
	pipreqs --no-pin . 

clean:
	rm requirements.txt

.PHONY: dep, clean