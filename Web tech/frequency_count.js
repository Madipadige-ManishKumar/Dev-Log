function findMostFrequentItem(arr) {
    const frequencyMap = {};
    let maxCount = 0;
    let mostFrequentItem = null;

    // Count the frequency of each item in the array
    for (const item of arr) {
        frequencyMap[item] = (frequencyMap[item] || 0) + 1;
        if (frequencyMap[item] > maxCount) {
            maxCount = frequencyMap[item];
            mostFrequentItem = item;
        }
    }

    return `${mostFrequentItem} (${maxCount} times)`;
}

// Sample array
var arr1 = [3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3];

// Find and display the most frequent item
document.write(findMostFrequentItem(arr1));
