#!/bin/ruby



Dir.foreach('input/.') do |item|
    #takes all files from input folder, ignoring root directory and mac hidden folder
    next if item == '.' or item == '..' or item == '.DS_Store'

    datafile = File.open("input/#{item}", "r")

    data = ""
    taxaname = ""

    datafile.each_with_index do |line, index|

        next if index <= 4
        next if line.start_with?(/\s/, "WWW.NATURE.COM", ";")

        if line.start_with?(/[A-Z]/)
            newtaxaname = line

            unless taxaname == ""
                file = File.new("output/#{taxaname}", "w")
                file.puts(data)
                file.close
            end

            data = ""
            taxaname = line

        else
            
            data = data + line

        end



        


    end






end