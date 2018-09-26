function [ AvgImg, height, width ] = ComputeAvgImg( filepath, start_index, end_index, step_size, T_amb, T_tar, file_out_path )
  nImg = 1 + int16((end_index - start_index)/ step_size);
  
  filetype = sprintf( '%d.pgm', start_index );
  filename = strcat( filepath, filetype );
      
  [Img_Mat, height, width] = ReadImage2(filename);
      
  Img_Array = zeros( height, width, nImg );
  Img_Acc = zeros( height, width );
  AvgImg = zeros(height,width);
  
  j = 1;
  for i = start_index : step_size : end_index
    filetype = sprintf( '%d.pgm', i );
    filename = strcat( filepath, filetype );
      
    [Img_Mat, height, width] = ReadImage2(filename);
      
    Img_Array(:,:,j) = Img_Mat;
      
    j = j + 1;
  end
  
  for i = 1:1:nImg
    Img_Acc = Img_Acc + Img_Array(:,:,i);
  end
   
  AvgImg = round(Img_Acc ./ double(nImg));
      
  filetype = sprintf( 'AvgImg_%d_%d.pgm', T_amb, T_tar );
  file_out = strcat( file_out_path, filetype );
  dlmwrite( file_out, AvgImg, ' ' );
end