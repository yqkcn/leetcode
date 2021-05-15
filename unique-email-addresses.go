package main

import "strings"

func numUniqueEmails(emails []string) int {
	counter := make(map[[2]string]bool)
	for _, email := range emails {
		_email := strings.Split(email, "@")
		local := strings.Split(_email[0], "+")[0]
		local = strings.Replace(local, ".", "", -1)
		counter[[2]string{local, _email[1]}] = true
	}

	return len(counter)
}
