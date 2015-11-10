function centroids = init_centroids(X,K) 
    
    centroids = zeros(K,size(X,2));
    
    % Shuffline all the input pixels
    randidx = randperm(size(X,1));
    
    % Select the firt K randomly from this set
    
    centroids = X(randidx(1:K),:);
end
