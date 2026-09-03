#!/usr/bin/env ruby

line = ARGV[0].to_s
if line =~ /\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/
  puts "#{$1},#{$2},#{$3}"
end
