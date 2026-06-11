(function() {
    const debugDiv = document.createElement('div');
    debugDiv.style.position = 'fixed';
    debugDiv.style.top = '10px';
    debugDiv.style.left = '10px';
    debugDiv.style.background = 'rgba(0,0,0,0.95)';
    debugDiv.style.color = '#00ff00';
    debugDiv.style.padding = '15px';
    debugDiv.style.fontFamily = 'monospace';
    debugDiv.style.fontSize = '12px';
    debugDiv.style.zIndex = '99999';
    debugDiv.style.lineHeight = '1.4';
    debugDiv.style.border = '2px solid #00ff00';
    
    const getInfo = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return sel + ': NOT FOUND';
        const r = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        return sel + ' -\n  rect: top=' + r.top.toFixed(1) + ', bottom=' + r.bottom.toFixed(1) + ', height=' + r.height.toFixed(1) + ', width=' + r.width.toFixed(1) + '\n  css: height=' + style.height + ', position=' + style.position + ', overflow=' + style.overflow;
    };

    debugDiv.innerText = [
        'LAYOUT DEBUG:',
        getInfo('.volvo-maps-section'),
        getInfo('.swiper-volvo-maps'),
        getInfo('.swiper-volvo-maps .swiper-slide-active'),
        getInfo('.swiper-volvo-maps .swiper-slide-active .volvo-map-slide-inner'),
        getInfo('.swiper-volvo-maps .swiper-slide-active .volvo-map-image'),
    ].join('\n\n');
    document.body.appendChild(debugDiv);
})();
