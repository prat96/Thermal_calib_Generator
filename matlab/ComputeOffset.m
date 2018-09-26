function [ OffsetMat ] = ComputeOffset ( GainMat, AvgImgMat, OffsetPath, T_amb )
  GI = GainMat.*AvgImgMat; % GI => Gain Corrected Image
  medianGI = median(GI(:));
  OffsetMat =  round( 100000 *  ( GI - medianGI )) ./ 100000; % This is Offset Coefficient for the image to which nuc has to apply
  
  OffsetName = sprintf( 'Offset_Mats/Offset_%d.mat', T_amb );
  OffsetFile = strcat( OffsetPath, OffsetName );
  dlmwrite( OffsetFile, OffsetMat, ' ' );
end
