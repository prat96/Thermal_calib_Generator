clear all;

%%%%%%%%%% User Controlled Parameters %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

GAIN_CALIB = 0;
OFFSET_CALIB = 1;
BOLOMETER_CALIB = 0;
POLYFIT_OFFSET_CALIB = 0;

HEIGHT = 480;
WIDTH = 650;
BOLOMETER_PREFIX = 3;
BOLOMETER_SUFFIX = 7;

% Gain Calibration
Gain_Amb_T = 25;
Gain_Ref_T1 = 15;
Gain_Ref_T2 = 45;

% Offset Bolometer and Polyfit Calibration
Offset_Amb_T = 20;

Offset_Calib_T_lo = 20;
Offset_Calib_T_hi = 40;
Offset_Calib_Tstep = 5;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

GAINPATH_REFIMG_1 = 'Calibration_Data/Gain_Data/';
GAINPATH_REFIMG_2 = 'Calibration_Data/Gain_Data/';
GAINPATH_RAWIMG_1 = 'Calibration_Data/Gain_Data/Ref1/';
GAINPATH_RAWIMG_2 = 'Calibration_Data/Gain_Data/Ref2/';
GAIN_PATH = 'Calibration_Data/Gain_Data/';

COMPUTE_AVG_IMG = 1;
RAW_IMG_PATH = 'Calibration_Data/Offset_Data/RawImgs/';
AVGIMG_PATH = 'Calibration_Data/Offset_Data/AvgImgs/';
start_index = 0;
end_index = 59;
step_size = 5;

PRUNE_IMAGE = 1;

OFFSET_PATH = 'Calibration_Data/Offset_Data/';


if( GAIN_CALIB )
  pruned_width = WIDTH - ( BOLOMETER_PREFIX + BOLOMETER_SUFFIX );
  
  [ AvgImg1, height, width ] = ComputeAvgImg( GAINPATH_RAWIMG_1, start_index, end_index, step_size, Gain_Amb_T, Gain_Ref_T1, GAINPATH_REFIMG_1 );
  [ PrunedAvgImg1 ] = PruneMatrix( AvgImg1, height, width, BOLOMETER_PREFIX, BOLOMETER_SUFFIX );
  
  [ AvgImg2, height, width ] = ComputeAvgImg( GAINPATH_RAWIMG_2, start_index, end_index, step_size, Gain_Amb_T, Gain_Ref_T2, GAINPATH_REFIMG_2 );
  [ PrunedAvgImg2 ] = PruneMatrix( AvgImg2, height, width, BOLOMETER_PREFIX, BOLOMETER_SUFFIX );
  
  
  Gain_Cutoff = 2.0;
  [ GainMat ] = ComputeGain( PrunedAvgImg1, PrunedAvgImg2, GAIN_PATH, HEIGHT, pruned_width, Gain_Cutoff, Gain_Ref_T1, Gain_Ref_T2 );
end

if( OFFSET_CALIB )
  GainName = sprintf( 'GainMat_%d_%d.mat', Gain_Ref_T1, Gain_Ref_T2 ); 
  GainFile = strcat( GAIN_PATH, GainName );
  GainMat = dlmread( GainFile, ' ' );
  
  pruned_width = WIDTH - ( BOLOMETER_PREFIX + BOLOMETER_SUFFIX );

  [ AvgImg, height, width ] = ComputeAvgImg( RAW_IMG_PATH, start_index, end_index, step_size, Offset_Amb_T, Offset_Amb_T, AVGIMG_PATH );
  [ PrunedAvgImg ] = PruneMatrix( AvgImg, height, width, BOLOMETER_PREFIX, BOLOMETER_SUFFIX );
 
  [ OffsetMat ] = ComputeOffset ( GainMat, PrunedAvgImg, OFFSET_PATH, Offset_Amb_T );
end

if( BOLOMETER_CALIB)
  [ bolometer_coefficients ] = ComputeBolometerPolynomial( AVGIMG_PATH, Offset_Calib_T_lo, Offset_Calib_T_hi, Offset_Calib_Tstep, HEIGHT, WIDTH, BOLOMETER_PREFIX, BOLOMETER_SUFFIX )
end   

if( POLYFIT_OFFSET_CALIB )
  pruned_width = WIDTH - ( BOLOMETER_PREFIX + BOLOMETER_SUFFIX );
  [ polyfit_coeff1, polyfit_coeff2, polyfit_coeff3 ] = ComputeOffsetPolynomial( OFFSET_PATH, HEIGHT, pruned_width, Offset_Calib_T_lo, Offset_Calib_T_hi, Offset_Calib_Tstep );
end