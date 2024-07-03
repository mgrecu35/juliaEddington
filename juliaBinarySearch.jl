function find_closest(rv, r)
    n = length(rv) # length of array rv
    # r is the actual value
    if r <= rv[1]
        return 1
    elseif r >= rv[n]
        return n
    end
    
    low, high = 1, n
    while low <= high
        mid = div(low + high, 2)
        if rv[mid] == r
            return mid
        elseif rv[mid] < r
            low = mid + 1
        else
            high = mid - 1
        end
    end
    
    if low > n
        return n
    elseif low < 1
        return 1
    end
    
    if abs(rv[low] - r) < abs(rv[high] - r)
        return low
    else
        return high
    end
end