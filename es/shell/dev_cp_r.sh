cp_r.sh /home/src /link-src/${mydir:=nlp}

# notebook目录.py文件覆盖, .ipynb不覆盖
[ ${mydir:=nlp} == 'nlp' ] && \
    mkdir -p /home/dataset/notebook && \
    rm -rf /link-src/nlp/notebook && \
    ln -sf /home/dataset/notebook /link-src/nlp/ && \
    cp -f /home/src/notebook/*.py /link-src/nlp/notebook/ && \
    false | cp -i /home/src/notebook/*.ipynb /link-src/nlp/notebook/ > /dev/null 2>&1 && \
    echo "re-linked notebook"