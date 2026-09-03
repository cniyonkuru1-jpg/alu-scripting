#!/usr/bin/env ruby

str = ARGV[0].to_s
puts str.scan(/[A-Z]/).join
