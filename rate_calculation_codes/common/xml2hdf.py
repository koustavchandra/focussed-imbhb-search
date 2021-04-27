'''
This program converts a standard sngl_inspiral table based injection file
into an hdf5 format. The code is a replica of `pycbc_coinc_hdfinjfind`
'''

import logging, numpy, h5py, os
from glue.ligolw import ligolw, table, lsctables, utils as ligolw_utils

log_level = logging.INFO
logging.basicConfig(level=log_level,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class LIGOLWContentHandler(ligolw.LIGOLWContentHandler):
    pass
lsctables.use_in(LIGOLWContentHandler)

def hdf_append(f, key, value):
    if key in f:
        tmp = numpy.concatenate([f[key][:], value])
        del f[key]
        f[key] = tmp
    else:
        f[key] = value
        
def xml_to_hdf(table, hdf_file, hdf_key, columns):
    """ Save xml columns as hdf columns, only float32 supported atm.
    """
    for col in columns:
        # Look for key in the form 'a:b' where we want to 
        # read data from column a but store it as named output 'b'
        # This is used to keep the output consistent where the input may not
        # depending on the injection file format (xml vs hdf)
        if ':' in col:
            col, new_col = col.split(':')
        else:
            new_col = col
        key = os.path.join(hdf_key, new_col)
        hdf_append(hdf_file, key, numpy.array(table.get_column(col),
                                        dtype=numpy.float32))
        

path_to_directory = '/home/koustav.chandra/O3/XML2hdf/XMLs/'

for file in os.listdir(path_to_directory):
    if file.endswith('.xml.gz'):
        injection_file = path_to_directory + file
        output_file = file.replace('.xml.gz', '.h5')
        fo = h5py.File(output_file, 'w')
        logging.info('Reading file {}'.format(injection_file))
        indoc = ligolw_utils.load_filename(injection_file, False,
                                           contenthandler=LIGOLWContentHandler)
        sim_table = table.get_table(indoc, lsctables.SimInspiralTable.tableName)
        inj_time = numpy.array(sim_table.get_column('geocent_end_time') +
                               1e-9 * sim_table.get_column('geocent_end_time_ns'),
                               dtype=numpy.float64)

        ninj = len(sim_table)
        columns = ['mass1', 'mass2', 'spin1x', 'spin1y',
                   'spin1z', 'spin2x', 'spin2y', 'spin2z',
                   'inclination', 'polarization', 'coa_phase',
                   'latitude:dec', 'longitude:ra', 'distance', 'f_lower','alpha6']
        xml_to_hdf(sim_table, fo, 'injections', columns)
        hdf_append(fo, 'injections/tc', inj_time)

logging.info('Finished!')        
