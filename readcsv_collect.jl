using CSV
using DataFrames
using PrettyTables

file_path = "data_with_classes.csv"
df = CSV.read(file_path, DataFrame)

global matclass1 = Array{Float64,2}(undef, 0, size(df, 2) - 1)
global matclass2 = Array{Float64,2}(undef, 0, size(df, 2) - 1)
global matclass3 = Array{Float64,2}(undef, 0, size(df, 2) - 1)

for row in eachrow(df)
    global matclass1, matclass2, matclass3
    data = collect(row[1:end-1])'
    
    if row[end] == 1
        matclass1 = vcat(matclass1, data)
    elseif row[end] == 2
        matclass2 = vcat(matclass2, data)
    elseif row[end] == 3
        matclass3 = vcat(matclass3, data)
    end
end

pretty_table(matclass1, title="Matrix 1")
pretty_table(matclass2, title="Matrix 2")
pretty_table(matclass3, title="Matrix 3")
