from bs4 import BeautifulSoup

html = '''
<gfg-tab slot="tab">Python</gfg-tab>
<gfg-panel slot="panel" data-code-lang="python3">
    <code class="language-python3">
    <div class="highlight">
    <pre><span></span><span class=c1># Python program for implementation of Selection</span>
<span class=c1># Sort</span>
<span class=n>A</span> <span class=o>=</span> <span class=p>[</span><span class=mi>64</span><span class=p>,</span> <span class=mi>25</span><span class=p>,</span> <span class=mi>12</span><span class=p>,</span> <span class=mi>22</span><span class=p>,</span> <span class=mi>11</span><span class=p>]</span>

<span class=c1># Traverse through all array elements</span>
<span class=k>for</span> <span class=n>i</span> <span class=ow>in</span> <span class=nb>range</span><span class=p>(</span><span class=nb>len</span><span class=p>(</span><span class=n>A</span><span class=p>)</span><span class=o>-</span><span class=mi>1</span><span class=p>):</span>

    <span class=c1># Find the minimum element in remaining </span>
    <span class=c1># unsorted array</span>
    <span class=n>min_idx</span> <span class=o>=</span> <span class=n>i</span>
    <span class=k>for</span> <span class=n>j</span> <span class=ow>in</span> <span class=nb>range</span><span class=p>(</span><span class=n>i</span><span class=o>+</span><span class=mi>1</span><span class=p>,</span> <span class=nb>len</span><span class=p>(</span><span class=n>A</span><span class=p>)):</span>
        <span class=k>if</span> <span class=n>A</span><span class=p>[</span><span class=n>min_idx</span><span class=p>]</span> <span class=o>&gt;</span> <span class=n>A</span><span class=p>[</span><span class=n>j</span><span class=p>]:</span>
            <span class=n>min_idx</span> <span class=o>=</span> <span class=n>j</span>

    <span class=c1># Swap the found minimum element with </span>
    <span class=c1># the first element        </span>
    <span class=n>A</span><span class=p>[</span><span class=n>i</span><span class=p>],</span> <span class=n>A</span><span class=p>[</span><span class=n>min_idx</span><span class=p>]</span> <span class=o>=</span> <span class=n>A</span><span class=p>[</span><span class=n>min_idx</span><span class=p>],</span> <span class=n>A</span><span class=p>[</span><span class=n>i</span><span class=p>]</span>

<span class=c1># Driver code to test above</span>
<span class=nb>print</span> <span class=p>(</span><span class=s2>"Sorted array"</span><span class=p>)</span>
<span class=k>for</span> <span class=n>i</span> <span class=ow>in</span> <span class=nb>range</span><span class=p>(</span><span class=nb>len</span><span class=p>(</span><span class=n>A</span><span class=p>)):</span>
    <span class=nb>print</span><span class=p>(</span><span class=n>A</span><span class=p>[</span><span class=n>i</span><span class=p>],</span><span class=n>end</span><span class=o>=</span><span class=s2>" "</span><span class=p>)</span> 
</pre></div>
    </code>
</gfg-panel>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Extract the content inside the gfg-panel tag
panel_content = soup.find('gfg-panel').prettify()

# Alternatively, you can extract just the code inside the <pre> tag
code_content = soup.find('pre').text

# print("Full gfg-panel content:\n", panel_content)
print("\nExtracted code content:\n", code_content)
