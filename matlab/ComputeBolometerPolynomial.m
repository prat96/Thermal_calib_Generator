function [ bolometer_coefficients ] = ComputeBolometerPolynomial( filepath, T_lo, T_hi, T_step_size, height, width, prefix_cols, suffix_cols )  
  n_rows = 1 + int16(( T_hi - T_lo )/T_step_size);
  avg_bolometer_T_mat = zeros( n_rows, 2);

  index = 1;
  for i = T_lo : T_step_size : T_hi
    Temp = i;  %y_axis  
    filetype = sprintf( 'AvgImg_%d_%d.pgm', Temp, Temp );
    filename = strcat( filepath, filetype );
      
    Img_Mat = load(filename);
  
    bolometer_prefix_mat = Img_Mat( : , 1 : prefix_cols );
    bolometer_suffix_mat = Img_Mat( : , end - suffix_cols + 1 : end );

    bolometer_mat = [bolometer_prefix_mat , bolometer_suffix_mat];

    avg_bolometer_Temp = mean(mean(bolometer_mat));  %x_axis
  
    avg_bolometer_T_mat( index , 1 ) = avg_bolometer_Temp;
    avg_bolometer_T_mat( index , 2 ) = Temp;
  
    index = index + 1;
  end
  
  plot(avg_bolometer_T_mat(:,1),avg_bolometer_T_mat(:,2), '.');
  [ bolometer_coefficients , S ] = polyfit( avg_bolometer_T_mat(:,1), avg_bolometer_T_mat(:,2), 1 );
  
  fileout = sprintf( 'Calibration_Data/Bolometer_Data/BolometerPolynomial_%d_%d.mat', T_lo, T_hi );
  dlmwrite( fileout, bolometer_coefficients, ' ');
end
  
  