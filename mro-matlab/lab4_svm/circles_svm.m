function [ output_args ] = circles_svm()

    % generate data
    rng(1); % For reproducibility
    r = sqrt(rand(100,1)); % Radius
    t = 2 * pi * rand(100,1);  % Angle
    circle1 = [r .* cos(t), r .* sin(t)]; % Points

    r2 = sqrt(3 * rand(100,1) + 1); % Radius
    t2 = 2 * pi * rand(100,1);      % Angle
    circle2 = [r2 .* cos(t2), r2 .* sin(t2)]; % points
    
    figure;
    plot(circle1(:,1),circle1(:,2),'r.','MarkerSize',15)
    hold on
    plot(circle2(:,1),circle2(:,2),'b.','MarkerSize',15)
%     ezpolar(@(x)1);ezpolar(@(x)2);
    axis equal
    hold off
    
    circles = [ circle1 ; circle2 ];
    classes = ones(200, 1);
    classes(1:100) = 0;
    svmStruct = svmtrain(circles, classes,'ShowPlot',true);
    
    
    
    
end

