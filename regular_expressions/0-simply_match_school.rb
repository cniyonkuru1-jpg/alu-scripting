#!/usr/bin/env ruby

argument = ARGV[0]

matches = argument.scan(/School/)
puts matches.join
