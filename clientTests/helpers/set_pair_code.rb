require_relative './ruby-client/features/step_definitions/step_helpers.rb'
CONSTANTS_FILE = File.dirname(__FILE__) + '/../constants.h'

code = get_claim_code_from_server

def read_file
  File.open(CONSTANTS_FILE, 'r') do |f|
    f.read
  end
end

def write_file(string)
  f = open(CONSTANTS_FILE, 'w')  
  f.write(string)
  f.close  
end

if code.length > 0
  constants = read_file
  write_file(constants.gsub(/@".*"/, "@\"#{code}\""))
else
  puts "there was an error getting the code"
  exit -1
end

