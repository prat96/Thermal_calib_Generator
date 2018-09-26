function [img,height,width] = ReadImage2(fn)
  f = fopen(fn, 'r');
  fscanf(f, 'P2\n');
  vals = fscanf(f, '%d'); % %lf
  fclose(f);

  height = vals(2);
  width = vals(1);
  img = uint16(zeros(height, width));
  row = 1;
  col = 1;
  for i = 4:size(vals, 1)
    img(row, col) = uint16(vals(i));
    if col == width
      row = row + 1;
      col = 1;
    else
      col = col + 1;
    end
  end
end