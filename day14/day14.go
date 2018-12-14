package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	n := "323081"
	l := len(n)
	recipes := []int{3, 7}
	a, b := 0, 1
	s := 2
outer:
	for {
		digits := make([]int, 0, 3)
		for _, d := range fmt.Sprintf("%v", recipes[a]+recipes[b]) {
			digits = append(digits, int(d)-'0')
		}

		for _, d := range digits {
			recipes = append(recipes, d)
			s += 1

			if len(recipes) <= l {
				continue
			}

			if strconv.Itoa(d) == n[len(n)-1:] {
				var k strings.Builder
				for u := len(recipes) - l; u < len(recipes); u++ {
					k.WriteString(strconv.Itoa(recipes[u]))
				}
				if k.String() == n {
					fmt.Println(s - l)
					break outer
				}
			}

		}
		a = (a + recipes[a] + 1) % len(recipes)
		b = (b + recipes[b] + 1) % len(recipes)
	}
}
