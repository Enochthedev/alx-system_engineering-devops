#!/usr/bin/env ruby
input_str = ARGV[0]
matches = input_str.scan(/[A-Z]+/)
puts matches.join('')
