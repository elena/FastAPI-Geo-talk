import{d as _,i as d,a as p,u as h,b as u,c as m,e as f,f as n,g as t,t as o,h as s,F as g,r as v,n as y,j as x,o as l,k as b,l as k,m as P,p as N,q as w,_ as S}from"./index-fbde8d53.js";import{N as V}from"./NoteDisplay-8ba433bd.js";const j={class:"m-4"},A={class:"mb-10"},C={class:"text-4xl font-bold mt-2"},F={class:"opacity-50"},L={class:"text-lg"},T={class:"font-bold flex gap-2"},B={class:"opacity-50"},D=t("div",{class:"flex-auto"},null,-1),H={key:0,class:"border-gray-400/50 mb-8"},z=_({__name:"PresenterPrint",setup(E){d(p),h(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),u({title:`Notes - ${m.title}`});const i=f(()=>x.map(a=>{var r;return(r=a.meta)==null?void 0:r.slide}).filter(a=>a!==void 0&&a.noteHTML!==""));return(a,r)=>(l(),n("div",{id:"page-root",style:y(s(w))},[t("div",j,[t("div",A,[t("h1",C,o(s(m).title),1),t("div",F,o(new Date().toLocaleString()),1)]),(l(!0),n(g,null,v(s(i),(e,c)=>(l(),n("div",{key:c,class:"flex flex-col gap-4 break-inside-avoid-page"},[t("div",null,[t("h2",L,[t("div",T,[t("div",B,o(e==null?void 0:e.no)+"/"+o(s(b)),1),k(" "+o(e==null?void 0:e.title)+" ",1),D])]),P(V,{"note-html":e.noteHTML,class:"max-w-full"},null,8,["note-html"])]),c<s(i).length-1?(l(),n("hr",H)):N("v-if",!0)]))),128))])],4))}}),q=S(z,[["__file","/media/elena/seryy-alpha/elena/home/org_ro_participant/Evnt_conference_PyConAU/2023-talk-FastAPI/FastAPI-Geo-talk/fastapi-geo/node_modules/@slidev/client/internals/PresenterPrint.vue"]]);export{q as default};
