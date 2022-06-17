data_dir = '/home/remi/github/BIDS-matlab/lib/bids-methods/demos/data';

templates_dir = '/home/remi/github/BIDS-matlab/lib/bids-methods/templates';

partials_path = '/home/remi/github/BIDS-matlab/lib/bids-methods/partials';

%% PET

BIDS = bids.layout(fullfile(data_dir, 'pet001'));

pet_metadata = bids.query(BIDS, 'metadata', 'modality', 'pet', 'suffix', 'pet');

output = octache(fullfile(templates_dir, 'pet.mustache'), ...
                 'data', pet_metadata, ...
                 'partials_path', partials_path, ...
                 'partials_ext', 'mustache', ...
                 'warn', true, ...
                 'keep', true);

anat_metadata = bids.query(BIDS, 'metadata', 'modality', 'anat');

output = octache(fullfile(templates_dir, 'anat.mustache'), ...
                 'data', anat_metadata, ...
                 'partials_path', partials_path, ...
                 'partials_ext', 'mustache', ...
                 'warn', true, ...
                 'keep', true);