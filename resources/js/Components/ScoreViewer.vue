<template>
  <div>
    <div ref="viewer" class="viewer"></div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { getDocument } from "pdfjs-dist";
import { GlobalWorkerOptions } from "pdfjs-dist/lib/pdf";

GlobalWorkerOptions.workerSrc = "/js/pdf.worker.min.js";

export default {
  props: {
    src: String,
  },
  setup(props) {
    const viewer = ref(null);

    onMounted(async () => {
      const pdf = await getDocument({
    url: props.src,
    cMapUrl: "/cmaps/",
    cMapPacked: true,
    useWorkerFetch: false,
  }).promise;

      for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const canvas = document.createElement("canvas");
        const viewport = page.getViewport({ scale: 1 });

        canvas.width = viewport.width;
        canvas.height = viewport.height;

        const context = canvas.getContext("2d");
        const renderContext = {
          canvasContext: context,
          viewport: viewport,
        };

        await page.render(renderContext).promise;

        viewer.value.appendChild(canvas);
      }

      $(viewer.value).turn({
        width: "100%",
        height: "100%",
        autoCenter: true,
      });
    });

    return { viewer };
  },
};
</script>


<style scoped>
.viewer {
  width: 100%;
  height: 600px;
  overflow: hidden;
}
</style>
