#!/usr/bin/env ruby

str = ARGV[0].to_s
if str =~ /\A\d{10}\z/
  puts str
end
