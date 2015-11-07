A = double(imread('bird_small.png'));
 
%A is now a matrix of size 128*128*3
%We'll reshape this matrix A into a matrix of dimension m*3 where m will be
%128*128 i.e. the number of pixels.

A = A/255; %Normalizing all values from 0 to 1

%Reshaping

A_size = size(A);

X = reshape(A, A_size(1)*A_size(2),3);

%Now find the top 16 colours 
K = 16;

% i.e. we take the number of clusters to be 16

%Initializing the centroids

in_centroids = init_centroids(X,K);

%disp('Initialy, the centroids chosen');
%disp(in_centroids);

% Run K-means now

% we suppose that the k-means algorithm wll converge in 10 iterations
max_iterations = 10;

[centroids, idx] = kmeans(X,in_centroids,max_iterations);

%disp('The final centroids are ' );
%disp(centroids);

% Recover the image with new values
X_recovered = centroids(idx,:);
X_recovered = reshape(X_recovered,A_size(1), A_size(2), 3);
imshow(X_recovered);

