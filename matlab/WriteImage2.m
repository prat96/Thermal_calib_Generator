function WriteImage2(img, img_path, height, width )
  f = fopen(img_path, 'w');
  fprintf(f, 'P2\n');
  fprintf(f, '%d %d\n16383\n', width, height);

  row = 1;
  col = 1;
  for i = 1 : height*width
    fprintf(f, '%d ', uint16(img(row, col)));
    if col == width
      row = row + 1;
      col = 1;
    else
      col = col + 1;
    end
  end
  fclose(f);
end