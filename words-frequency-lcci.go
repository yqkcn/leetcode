package main

type WordsFrequency struct {
	freq map[string]int
}

func Constructor(book []string) WordsFrequency {
	freq := make(map[string]int)
	for _, word := range book {
		freq[word]++
	}
	return WordsFrequency{freq: freq}
}

func (this *WordsFrequency) Get(word string) int {
	return this.freq[word]
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * obj := Constructor(book);
 * param_1 := obj.Get(word);
 */
