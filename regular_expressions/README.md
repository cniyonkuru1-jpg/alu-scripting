# Regular expressions

Ruby scripts that use regular expressions (Oniguruma, the default Ruby engine).
Each script takes one argument and prints what the regex matches:

```ruby
puts ARGV[0].scan(/regex/).join
```

## Files

| File | What it does |
|------|--------------|
| `0-simply_match_school.rb` | Matches `School` |
| `1-repetition_token_0.rb` | Matches `hbtn` with 2 to 5 `t` (`hbttn` ... `hbttttn`) |
| `2-repetition_token_1.rb` | Matches `hbtn` with 1 to 4 `t` |
| `3-repetition_token_2.rb` | Matches `hbtn` with one or more `t` |
| `4-repetition_token_3.rb` | Matches `hbtn` with zero or more `t` (no square brackets) |
| `5-beginning_and_end.rb` | Matches a string that starts with `h`, ends with `n`, with any single character between |
| `6-phone_number.rb` | Matches a 10 digit phone number |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Matches only capital letters |
| `8-textme.rb` | Prints `[SENDER],[RECEIVER],[FLAGS]` from a TextMe log line |
| `9-passed_linkedin_regex_challenge.jpg` | Screenshot of the LinkedIn regex puzzle (to add) |

## Usage

```
$ ./5-beginning_and_end.rb h8n
h8n
$ ./6-phone_number.rb "415-504-9898"

$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?"
WHATSAY
```

## Requirements

- Ubuntu 20.04 LTS, Ruby
- Every script starts with `#!/usr/bin/env ruby` and is executable
- All files end with a new line
