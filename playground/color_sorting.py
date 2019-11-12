
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    min_positions = list()
    
    list_of_darkness = list()
    for intensity in list_of_intensities:
        list_of_darkness.append(sum(intensity))
    
    for pos, element in enumerate(list_of_darkness):
        if pos == 0:
            continue
        if pos == len(list_of_darkness) - 1:
            continue
        if list_of_darkness[pos - 1] > element < list_of_darkness[pos + 1]:
            min_positions.append(pos)
    return [list_of_intensities[x] for x in min_positions]
