package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	var rawData, err = os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Could not read file", err)
		return
	}

	var rawSeperatedReports = strings.Split(string(rawData[:len(rawData) - 1]), "\n")

	var reports [][]int
	var rawSeperatedReport []string

	for _, rawReport := range rawSeperatedReports {
		rawSeperatedReport = strings.Split(rawReport, " ")
		var report []int
		for _, rawData := range rawSeperatedReport {
			var data, err  = strconv.Atoi(rawData)
			if err != nil {
				fmt.Println("Could not convert data to int")
			}
			report = append(report, data)
		}
		reports = append(reports, report)
	}

	var safe int = 0
	for i := range reports {
		if isSafe(reports[i]) {
			safe += 1
		}
	}

	fmt.Println(safe)
}

func isSafe(report []int) bool{
	var increasing bool = report[0] < report[1]
	for i := 0; i < len(report) - 1; i++ {
		if increasing {
			if report[i] > report[i+1] || report[i+1] - report[i] < 1 || report[i+1] - report[i] > 3 {
				return false
			}
		} else {
			if report[i] < report[i+1] || report[i] - report[i+1] < 1 || report[i] - report[i+1] > 3 {
				return false
			}
		}
	}
	return true
}
