function [ GainMat ] = ComputeGain( I1, I2, GainPath, height, width, Gain_Cutoff, T_ref1, T_ref2 )
  I_ones = ones(height , width);
  
  mI1 = median(I1(:)); 
  mI2 = median(I2(:));

  GainMat = round( 100000 * (( ( mI1 - mI2 ) * I_ones ) ./ ( I1 - I2 ) )) ./ 100000;
  GainMat = abs(GainMat);
  
  % BadPixMat = isinf(GainMat);
  % GainMat(BadPixMat) = median(GainMat(:));
    
  % BadPixMat( GainMat > Gain_Cutoff ) = 1;
  GainMat( GainMat > Gain_Cutoff ) = Gain_Cutoff;
  
  GainName = sprintf( 'GainMat_%d_%d.mat', T_ref1, T_ref2 ); 
  GainFile = strcat( GainPath, GainName );
  dlmwrite( GainFile, GainMat, ' ' );
end 