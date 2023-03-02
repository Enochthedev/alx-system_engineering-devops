#!/usr/bin/env ruby
regex = /School/
input = ARGV[0]

matches = input.scan(regex)

if !matches.empty?
  puts matches.join('')
end

