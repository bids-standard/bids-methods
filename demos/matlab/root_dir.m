function value = root_dir()

  value = fullfile(fileparts(mfilename('fullpath')), '..', '..');

end
