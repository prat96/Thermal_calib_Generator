function [ Pruned_Mat ] = PruneMatrix( Raw_Mat, height, width, prefix, suffix )
  Pruned_Mat = Raw_Mat( : , prefix + 1 : end - suffix );
end