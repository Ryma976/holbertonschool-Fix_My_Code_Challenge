#!/usr/bin/env ruby

numbers = ARGV.select { |arg| arg.match?(/\A-?\d+\z/) }.map(&:to_i)

numbers.sort.each do |number|
  puts number
end
