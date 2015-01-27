function [ ] = cities( )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

%     data = load('cities_distances.txt', '-ascii');
%     data
%     yourVariable = importdata('cities_distances.txt', '\t', 1);
%     yourVariable
    
    distances = csvread('distances.txt', 1, 1);
    sim = mdscale(distances, 2, 'Options', statset('MaxIter', 400));
    labels = cell(24,1);
    labels = { 'Barcelona';'Belgrade';'Berlin';'Brussels';'Bucharest';'Budapest';'Copenhagen';'Dublin';'Hamburg';'Istanbul';'Kiev';'London';'Madrid';'Milan';'Moscow';'Munich';'Paris';'Prague';'Rome';'Saint Petersburg';'Sofia';'Stockholm';'Vienna';'Warsaw' } 
    scatter(sim(:, 1), sim(:, 2))
    for i = 1 : size(labels, 1)
        
        text(sim(i,1), sim(i,2), labels(i, :))
    end
end

