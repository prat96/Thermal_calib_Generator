function [ coeff1, coeff2, coeff3 ] = ComputeOffsetPolynomial( offset_filepath, height, width, T_lo, T_hi, T_step_size )  
  n_datapoints = 1 + int16(( T_hi - T_lo )/T_step_size);
  
  pixOffset_Acc = zeros( n_datapoints, 3);

  Offset_Mat = zeros(height,width);
  Offset_Array= zeros(height,width,n_datapoints);
  Offset_Polynomial = zeros(height,width,3);

  j = 1;
  for i = T_lo : T_step_size : T_hi
    i = abs(i);
    
    filetype = sprintf( 'Offset_Mats/Offset_%d.mat', i );
    filename = strcat( offset_filepath, filetype );
  
    Offset_Mat = load(filename); 
    
    Offset_Array(:,:,j) = Offset_Mat;
    j = j + 1;
  end

  for i = 1 : 1 : height
    for j = 1 : 1 : width
      index = 1;
      for k = T_lo : T_step_size : T_hi
        Temp = k;                                                             
        pixOffset_Acc(index, 1)  = Offset_Array(i, j, index);           % y-axis
        pixOffset_Acc(index, 2) =  Temp;                                    % x-axis     
        index = index + 1;
      end
        
      [p,S] = polyfit( pixOffset_Acc(:,2), pixOffset_Acc(:,1), 2 );
      
      Offset_Polynomial(i,j,1) = p(1);
      Offset_Polynomial(i,j,2) = p(2);
      Offset_Polynomial(i,j,3) = p(3);
    end
  end
  
  coeff1 = Offset_Polynomial(:,:,1);
  coeff2 = Offset_Polynomial(:,:,2);
  coeff3 = Offset_Polynomial(:,:,3);

  OffsetFileName1 = sprintf( 'Offset_Polynomial/coeff1_%d_%d.mat', T_lo, T_hi );
  OffsetFile1 = strcat( offset_filepath, OffsetFileName1 );
  dlmwrite( OffsetFile1, coeff1, ' ' );
  
  OffsetFileName2 = sprintf( 'Offset_Polynomial/coeff2_%d_%d.mat', T_lo, T_hi );
  OffsetFile2 = strcat( offset_filepath, OffsetFileName2 );
  dlmwrite( OffsetFile2, coeff2, ' ' );
  
  OffsetFileName3 = sprintf( 'Offset_Polynomial/coeff3_%d_%d.mat', T_lo, T_hi );
  OffsetFile3 = strcat( offset_filepath, OffsetFileName3 );
  dlmwrite( OffsetFile3, coeff3, ' ' );
end